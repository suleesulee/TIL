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

/**/
/**/
/**/
/**/
/**/
/**/
/**/
/**/
/**/
