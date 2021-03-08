/*
Chapter 7_2
풀링

pool 패키지에는 버퍼가 있는 채널을 이용해 공유가 가능한 리소스의 풀을 생성, 리소스들을 원하는 개수만큼 고루틴에서
개별적으로 활용할 수 있는 기능을 작성한 코드가 모여있음
이 패턴은 DB연결, 메모리 버퍼 등 공유되는 리소스의 정적인 집합을 관리할때 특히 유용
고루틴이 리소스중 하나를 사용해야 할 경우 리소스를 할당받고 사용한 뒤 풀에 반환하는 구조로 동작함
*/

package pool

import (
	"errors"
	"io"
	"log"
	"sync"
)

//io.Closer 인터페이스는 반드시 구현
type Pool struct {
	m         sync.Mutex
	resources chan io.Closer            //이 채널은 버퍼가 있는 채널로 생성, 공유하기 위한 리소스를 보관하는 목적으로 사용
	factory   func() (io.Closer, error) //io.Closer인터페이스를 구현하는 어떤 타입의 리소스도 관리 가능
	closed    bool                      //pool 값이 종료중 또는 종료된것을 의미
}

var ErrPoolClosed = errors.New("풀이 닫힘") //error 타입의 인터페이스 변수

func New(fn func() (io.Closer, error), size uint) (*Pool, error) { //첫번째 매개변수 fn은 함수타입 io.Closer와 error을 리턴 ,두 번째 매개변수 size 는 채널의 크기 지정
	if size <= 0 { //size는 0과 같거나 작으면 안됨
		return nil, errors.New("풀의 크기가 작음")
	}

	return &Pool{ //size값이 정상이면 Pool을 초기화함 factory 함수는 fn이고 resources는 버퍼가 있는 채널
		factory:   fn,
		resources: make(chan io.Closer, size),
	}, nil

}

func (p *Pool) Acquire() (io.Closer, error) { //풀에서 사용가능한 리소스를 찾아주거나 없으면 생성하는 메서드
	select {
	case r, ok := <-p.resources:
		log.Println("리소스 획득:", "공유된 리소스")
		if !ok {
			return nil, ErrPoolClosed
		}
		return r, nil //리소스가 존재하면 해당 리소스를 할당
	default:
		log.Println("리소스 획득:", " 새로운 리소스")
		return p.factory() //factory함수를 통해 새로운 리소스를 생성
	}
}

func (p *Pool) Release(r io.Closer) { //풀에 리소스를 반환하는 메서드
	p.m.Lock()         //잠금설정
	defer p.m.Unlock() //함수 종료시 무조건 언락

	if p.closed { //풀이 닫혀있으면 리소스를 해제 close가 사용하는 것과 같은 뮤텍스
		r.Close() //closed를 읽으려는 시점과 Close 메서드에서 closed를 조작하는 시점이 같을 수 있어서 잠금
		return
	}

	select { //닫힌채널에 리소스를 돌려보내면 패닉이 발생하기에 잠금
	case p.resources <- r:
		log.Println("리소스 반환:", "리소스 큐에 반환")
	default:
		log.Println("리소스 반환", "리소스 해제")
		r.Close()
	}
}

func (p *Pool) close() { //풀을 종료하고 모든 리소스 해제하는 메서드
	p.m.Lock()         //잠금설정
	defer p.m.Unlock() //함수 종료시 무조건 언락

	if p.closed { //풀이 이미 닫혀있음 그냥 종료
		return
	}

	p.closed = true    //풀을 닫음
	close(p.resources) //리소스 해제전 채널을 먼저 닫음

	for r := range p.resources { //리소스 해제
		r.Close()
	}
}
