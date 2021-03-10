/*work 패키지*/
/*
work 패키지의 목적은 버퍼가 없는 채널을 이용하여 원하는 개수만큼의 작업을 동시적으로 실행할 수 있는 고루틴 풀을 생성하는 것
필요한 만큼의 고루틴을 실행할 작업큐 생성시 버퍼가 없는 채널을 활용하는 것이 좋다
버퍼가 없는 채널은 풀이 작업을 수행할때, 채널이 바빠 더 이상 작업을 받을 수 없을때 작업이 다시 풀로 돌아오는 시점을 정확히 알수있음

유실되거나 큐에 갇혀 실행되지 않는 상황이 발생안함
*/

package wg

import "sync"

type Worker interface { //Worker 인터페이스를 구현해야함
	Task()
}

type Pool struct { //Worker 인퍼테이스를 실행하는 고루틴이 풀을 제공하기 위한 Pool 구조체
	work chan Worker
	wg   sync.WaitGroup
}

func New(maxGoroutines int) *Pool {
	p := Pool{
		work: make(chan Worker), //버퍼가 없는 채널로 초기화
	}

	p.wg.Add(maxGoroutines)
	for i := 0; i < maxGoroutines; i++ {
		go func() {
			for w := range p.work {
				w.Task() //worker 채널에서 Worker 인터페이스 값을 받는 한 계속해서 for range 루프 진행 루프내에서 Task 메서드 호출
			}
			p.wg.Done() //채널이 닫힘 Done 메서드를 호출
		}()
	}
	return &p
}

func (p *Pool) Run(w Worker) { //Run메서드는 Worker 인터페이스 값을 work 채널로 보냄
	p.work <- w //버퍼가 없기에 반드시 고루틴 풀에 전달됨
}

func (p *Pool) Shutdown() {
	close(p.work) //work 채널을 닫음
	p.wg.Wait()   //풀에 저장된 모든 고루틴은 실행을 종료하고 Done을 호출..
	// Wait 메서드를 호출해 모든 고루틴이 실행을 종료할 때까지 대기
}

/**/
