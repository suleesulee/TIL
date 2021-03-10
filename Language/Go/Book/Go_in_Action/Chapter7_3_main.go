package main

import (
	"log"
	"sync"
	"time"
)

var names = []string{
	"a",
	"b",
	"c",
	"d",
	"e",
}

type namePrinter struct {
	name string
}

func (m *namePrinter) Task() { //Task 메서드를 선언해 Worker 인터페이스를 구현
	log.Println(m.name)
	time.Sleep(time.Second) //대기시킴
}

func main() {
	p := work.New(2) //두개의 작업 풀 생성

	var wg sync.WaitGroup
	wg.Add(100 * len(names))

	for i := 0; i < 100; i++ { //100개의 고루틴 생성 경쟁적으로 등록하는것 흉내
		for _, name := range names {
			np := namePrinter{
				name: name,
			}

			go func() {
				p.Run(&np) //실행할 작업 등록 Run메서드가 리턴되면 작업 처리된 것으로 간주 런 메소드 호출해서 namePrinter 값 풀에 등록
				wg.Done()  //Run메서드 리턴되면 실행
			}()
		}
	}
	wg.Wait() //모든 고루틴이 생성되면 Wait 호출 모든 고루틴이 풀에 등록되어 실행 완료때까지 대기

	p.Shutdown() //Wait메서드가 리턴되면 실행
}
