/*
경쟁상태(Race condition)

고루틴이 동기화 없이 공유된 자원에 접근하여 읽거나 쓰기를 시도하게 될때를 경쟁상태라고함
공유자원에 대한 읽기 및 쓰기 작업은 반드시 원자성을 가져야 함.


*/

/*
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var (
	counter int
	wg      sync.WaitGroup
)

func main() {
	wg.Add(2)

	go incCounter(1)
	go incCounter(2)

	wg.Wait()
	fmt.Println("result:", counter)
}

func incCounter(id int) {
	defer wg.Done()

	for count := 0; count < 2; count++ {
		value := counter
		runtime.Gosched()

		value++

		counter = value
	}
}
*/

/*
고루틴은 counter의 값을 복사하여 보관하다가 다른 고루틴으로 실행이 교체됨
원래의 고루틴이 다시 실행을 재개하면 counter변수의 값은 이미 변경되지만 고루틴은 값이 수정되었는지 모름
그래서 자신이 보유한 복사 값을 증가시킨후 counter변수에 대입하기에
다른 고루틴이 수행한 결과가 덮어써짐

Gosched 함수가 실행되면 스레드를 양보하기에 다른 고루틴이 실행됨
두 고루틴이 배타적으로 실행하는 경쟁상태에 놓임
Go는 코드 내 경쟁상태의 발생 가능성을 검사하는 도구를 제공

go build-race

데이터 경쟁을 유발시킨 고루틴을 알려준다
공유 자원 잠금 기법을 활용해 고루틴을 동기화 시킴
atomic, sync 패키지

*/
/*
package main

import (
	"fmt"
	"runtime"
	"sync"
	"sync/atomic"
)

var (
	counter int64
	wg      sync.WaitGroup
)

func main() {
	wg.Add(2)

	go incCounter(1)
	go incCounter(2)

	wg.Wait()

	fmt.Println("result:", counter)
}

func incCounter(id int) {
	defer wg.Done()

	for count := 0; count < 2; count++ {
		atomic.AddInt64(&counter, 1) //오직 한 시점에 오직 한개의 고루틴만이 변수에 접근가능

		runtime.Gosched()
	}

}
*/
/*고루틴이 원자성 함수를 호출하면 참조하는 변수에 대한 동기화가 자동적으로 수행됨*/

/*
atomic 패키지의 LoadInt64, StoreInt64 함수도 유용
*/

/*
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

var (
	shutdown int64
	wg       sync.WaitGroup
)

func main() {
	wg.Add(2)

	go doWork("A")
	go doWork("B")

	time.Sleep(1 * time.Second)

	fmt.Println("teminated")
	atomic.StoreInt64(&shutdown, 1) //종료 신호 플래그 생성

	wg.Wait()
}

func doWork(name string) {
	defer wg.Done()

	for {
		fmt.Printf("work : %s\n", name)
		time.Sleep(250 * time.Millisecond)

		//종료 플래그를 확인하고 실행 종료
		if atomic.LoadInt64(&shutdown) == 1 {
			fmt.Printf("finish :%s\n", name)
			break
		}
	}
}
*/

/*
LoadInt64를 이용해 shutdown 변수의 값을 확인
해당 함수는 shutdown 변수 값의 복사본을 안전하게 리턴
이 값이 1이면 고루틴은 루프를 탈출 후 실행 종료

StoreInt64 함수는 shutdown변수의 값을 변경 StoreInt64 함수를 호출하는 것과 같은 시점에 doWork함수를 실행하는 고루틴 중 하나가
LoadInt64함수를 호출하면 원자성 함수들은 함수 호출을 동기화
모든 작업이 경쟁상태에 놓이지 않고 안전하게 실행될 수 있도록 보장함
*/

/*
공유 자원에 대한 접근을 동기화 하는 방법은 뮤텍스가 있음
뮤텍스는 상호베타(mutual exclusion)의 개념에서 유래
뮤텍스는 코드 주변에 임계 지역(critical section)을 생성하여 해당 코드를 한 번에 하나의
고루틴만이 실행할 수 있도록 보장
*/

package main

import (
	"fmt"
	"runtime"
	"sync"
)

var (
	counter int
	wg      sync.WaitGroup
	mutex   sync.Mutex
)

func main() {
	wg.Add(2)

	go incCounter(1)
	go incCounter(2)

	wg.Wait()
	fmt.Printf("result: %d\n", counter)
}

func incCounter(id int) {
	defer wg.Done()

	for count := 0; count < 2; count++ {
		mutex.Lock()
		{
			value := counter
			runtime.Gosched()
			value++
			counter = value
		}
		mutex.Unlock()
	}
}

/*
mutex.Lock(), mutex.Unlock()
사이는 임계영역으로 한번의 하나의 고루틴만 접근가능
중괄호는 쓰던 안쓰던 상관 없음
lock이 걸리면 unlock이 호출될 때까지 다른 고루틴은 접근 불가능
*/
