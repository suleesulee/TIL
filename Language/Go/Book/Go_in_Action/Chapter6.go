/*
동시성

Go에서의 동시성은 함수들을 다른 함수들과 독립적으로 실행할 수 있는 것을 의미
고루틴으로 생성시 실행해야하는 함수로 예약된 후 논리 프로세스가 여력이 있을때 실행되는 독립적인 작업 단위로 취급
Go 런타임 스케쥴러는 코드에서 생성되어 프로세서가 개별적으로 처리해야할 모든 고루틴을 관리하기 위해 만들어진 소프트웨어
스케쥴러는 OS를 기반으로 동작하며 OS의 Thread를 고루틴을 실행하는 논리 프로세서에 바인딩됨
또한, 어떤 논리 프로세서상에서 얼마나 오래 실행 중인지를 추적하는데 필요한 모든 것을 관리

Go에서 동시성 처리 시 동기화는 CSP(Communicating Sequential Processes, 통신 순차 처리)라는 패러다임에서 비롯됨
CSP는 고루틴 사이에 데이터를 교환할 때 동시적 데이터 접속으로 부터 데이터를 잠그는 기법(세마포어, 모니터...)메시지를 전달
동기화와 메시지 교환을 위한 핵심 데이터 타입은 채널(Channel)임


Go런타임 스케쥴러는 고루틴을 논리적 프로세스를 통해 실행할 수 있도록 예약함
각 논리 프로세서는 하나의 OS Thread에 개별적으로 바인딩됨
하나의 논리프로세서만 존재한다 하여도 수천 이상의 고루틴을 동시적으로 실행해서 효율과 성능을 향상 가능

고루틴이 생성되고 실행 준비가 되면 스케쥴러의 범용 실행 큐(global run queue)에 들어가고
논리프로세서가 할당되어 해당 프로세서의 지역 실행 큐에 위치한다. 그리고 논리 프로세서가 자신을 실행할 때까지 대기

고루틴이 실행을 중단하는 시스템 콜을 수행할 경우 논리 프로세서로부터 Thread와 go routine이 분리 된 후 ,
Thread는 시스템 콜이 리턴될 때까지 대기함.package Go_in_Action
그러는 동안 논리 프로세서는 할당된 스레드가 없는 상태이며
스케쥴러가 새로운 스레드를 생성하여 논리 프로세서에 연결한 뒤 지역 실행 큐에서 다른 고루틴을 선택하여 실행
앞서 수행한 시스템 콜이 리턴되면 실행 중인 고루틴은 다시 지역 실행 큐로 이동함
다시 사용될 것을 대비해 고루틴이 실행 중인 스레드도 함께 보관
네트워크 I/O 콜은 처리과정이 다름
이 경우 고루틴은 논리 프로세서에서 분리되어 런타임에 통합된 네트워크 폴러(poller)로 이동
네트워크 폴러가 읽거나 쓰기 작업을 실행할 준비가 되면 고루틴이 다시 논리 프로세서에 연결되어 작업 시작

런타임의 프로그램당 최대 스레드의 개수는 기본적으로 10000개로 제한됨

동시성은 병렬성과 다른 개념
병렬성은 여러 개의 코드가 각기 다른 물리적 프로세서에서 동시에 실행되는것
동시성은 한 번에 여러 작업을 관리하는 것
병렬성에 대해 동시성이 성능이 좋음
이유는 OS와 HW에 가해지는 부담이 적어 시스템이 더 많은 일을 할 수 있음

고루틴을 병렬적으로 실행하고 싶다면 반드시 하나 이상의 논리적 프로세스를 사용해야함
논리 프로세서가 여러개라면 스케줄러가 고루틴을 논리 프로세서에 골고루 분배

진정한 의미의 병렬성은 물리적으로 다중 프로세서를 갖춘 머신에서 프로그램 실행해야함

*/

/*
package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	runtime.GOMAXPROCS(1)

	var wg sync.WaitGroup

	wg.Add(2) //2개의 Go routine이 동작

	fmt.Println("run Go routine")

	go func() {
		defer wg.Done()

		for cnt := 0; cnt < 3; cnt++ {
			for char := 'a'; char < 'a'+26; char++ {
				fmt.Printf("%c", char)
			}
		}
	}()

	go func() {
		defer wg.Done() //WaitGroup의 값을 감소 시킴 defer는 함수 종료 시 무조건 실행되는것을 보장

		for cnt := 0; cnt < 3; cnt++ {
			for char := 'A'; char < 'A'+26; char++ {
				fmt.Printf("%c", char)
			}
		}
	}()

	fmt.Println("Wait...")
	wg.Wait() //go routine이 완료 될 때까지 대기!

	fmt.Println("\n Program terminated")
}
*/

/*
스케쥴러 알고리즘에 따라 고루틴은 작업을 완료하기전에 실행이 중단된 후 다음 순서로 다시 예약되기도 함
오랫동안 잡고있는 것을 방지 (aging 방지)
*/

/*
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg sync.WaitGroup

func main() {
	runtime.GOMAXPROCS(1)

	wg.Add(2) //2개의 Go routine이 동작

	fmt.Println("run Go routine")
	go printPrime("A")
	go printPrime("B")

	fmt.Println("Wait...")
	wg.Wait() //go routine이 완료 될 때까지 대기!

	fmt.Println("\n Program terminated")
}

func printPrime(prefix string) {
	defer wg.Done()

next:
	for outer := 2; outer < 5000; outer++ {
		for inner := 2; inner > outer; inner++ {
			if outer%inner == 0 {
				continue next
			}
		}
		fmt.Printf("%s:%d\n", prefix, outer)
	}
	fmt.Println("fin : ", prefix)
}
*?
/*
함수를 고루틴처럼 실행하는 경우에도 일반적 함수 호출과 마찬가지로 매개변수 전달 가능
고루틴이 종료할 때 값 리턴은 불가

위 예제는 하나의 논리 프로세서상에서 고루틴을 동시에 실행함
*/

package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	runtime.GOMAXPROCS(2) //2개의 논리프로세서 할당

	var wg sync.WaitGroup

	wg.Add(2) //2개의 Go routine이 동작

	fmt.Println("run Go routine")

	go func() {
		defer wg.Done()

		for cnt := 0; cnt < 3; cnt++ {
			for char := 'a'; char < 'a'+26; char++ {
				fmt.Printf("%c", char)
			}
		}
	}()

	go func() {
		defer wg.Done() //WaitGroup의 값을 감소 시킴 defer는 함수 종료 시 무조건 실행되는것을 보장

		for cnt := 0; cnt < 3; cnt++ {
			for char := 'A'; char < 'A'+26; char++ {
				fmt.Printf("%c", char)
			}
		}
	}()

	fmt.Println("Wait...")
	wg.Wait() //go routine이 완료 될 때까지 대기!

	fmt.Println("\n Program terminated")
}
