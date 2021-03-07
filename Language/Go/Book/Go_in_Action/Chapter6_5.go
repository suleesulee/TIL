/*
채널(channel)
원자성 함수나 뮤텍스만이 Go에서 공유자원을 보호하며 경쟁상태를 피하는 유일한 방법은 아님
필요한 공유자원을 다른 고루틴에 보내거나 받아 고루틴 사이의 동기화를 지원하는 채널(channel)이 존재

고루틴 간 자원을 공유해야하는 경우 채널은 고루틴 사이를 연결하는 파이프처럼 동작
데이터 교환에 있어 동기화를 보장하는 메커니즘 제공
공유 데이터는 타입을 명시해야함 내장, 사용자 정의, 구조체, 참조 타입틔 값과 포인터는 모두 채널을 통해 공유 가능

unbuff := make(chan int)
buff := make(chan string, 10)

버퍼가 없는 채널 있는 채널 생성가능
채널을 통해 값이나 포인터를 보내려면 <-연산자를 사용

채널에 값 보내기
buff := make(chan string, 10)
buff <- "Gopher"

값 전달받기
value := <- buff
*/

/*
버퍼가 없는 채널은 값을 전달 받기 전에 어떤 값을 얼마나 보유할 수 있는지 크기가 결정되지 않은 채널
채널에 값을 보내거나 받기 전에 값을 전달하는 고루틴과 전달 받는 고루틴이 같은 시점에 채널을 사용할 준비가 되어있어야함

두 고루틴이 같은 시점에 준비되어 있지 않다면 대기작업을 시작
그러면 고루틴은 필요한 작업을 수행할 수 없다
*/
/*
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

func init() {
	rand.Seed(time.Now().UnixNano())
}

func main() {
	court := make(chan int)

	wg.Add(2)

	go player("Nadal", court)
	go player("jokv", court)

	court <- 1

	wg.Wait()
}

func player(name string, court chan int) {
	defer wg.Done()

	for {
		ball, ok := <-court
		if !ok {
			fmt.Printf("%s 선수가 승리\n", name)
			return
		}

		n := rand.Intn(100)
		if n%13 == 0 {
			fmt.Printf("%s 선수가 공을 받아치치 못함\n", name)

			close(court)
			return
		}

		fmt.Printf("%s 선수가 %d 번째 공을 받아침\n", name, ball)
		ball++

		court <- ball
	}
}
*/
/*
버퍼가 있는 채널
고루틴이 값을 받아가기 전까지 채널에 보관할 수 있는 값의 개수를 저장 가능함
보내고 받는 동작이 동시에 이루어지지 않아도 됨
값을 받는 작업의 작업은 채널내 받을 값이 없을 때만 실행됨
값을 보내는 작업의 작업은 채널 내 버퍼가 가득 찼을때 실행
버퍼가 없는 채널은 값을 보내고 받는 동작이 동시에 이루어지는 것을 보장하지만 버퍼가 있는 채널은 보장 안함
*/

package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const (
	numberGoroutines = 4
	taskLoad         = 10
)

var wg sync.WaitGroup

func init() {
	rand.Seed(time.Now().Unix())
}

func main() {
	tasks := make(chan string, taskLoad)

	wg.Add(numberGoroutines)
	for gr := 1; gr <= numberGoroutines; gr++ {
		go worker(tasks, gr)
	}

	for post := 1; post <= taskLoad; post++ {
		tasks <- fmt.Sprintf("Work: %d", post)
	}

	close(tasks)
	//채널이 닫혀도 각 고루틴들은 더 이상 받을 값이 없을때까지 계속 값을 받음

	wg.Wait()
}

func worker(tasks chan string, worker int) {
	defer wg.Done()

	for { //무한루프 while(1)
		task, ok := <-tasks //채널에서 실행할 작업을 받는 작업을 수행하는 동안 잠금 상태
		if !ok {            //ok 플래그를 검사하여 채널이 비었거나 닫혔는지 확인 true는 채널에서 받은 값이 유효한 값이라고 판단함. false는 종료
			fmt.Printf("Worker: %d : terminated\n", worker)
			return
		}

		fmt.Printf("Worker: %d : Start work: %s\n", worker, task)

		sleep := rand.Int63n(100)
		time.Sleep(time.Duration(sleep) * time.Millisecond)

		fmt.Printf("Worker: %d : Work Complite: %s\n", worker, task)
	}
}

/**/
/**/
/**/
/**/
/**/
/**/
/**/
/**/
