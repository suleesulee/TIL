package main

import (
	"io"
	"log"
	"math/rand"
	"sync"
	"sync/atomic"
	"time"
)

const (
	maxGoroutines   = 25
	pooledResources = 2
)

type dbConnection struct {
	ID int32
}

//Close 메서드
func (dbConn *dbConnection) Close() error {
	log.Println("닫힘: DB연결", dbConn.ID)
	return nil
}

var idCounter int32

//팩토리 메서드
func createConnection() (io.Closer, error) {
	id := atomic.AddInt32(&idCounter, 1)
	log.Println("생성: New db 연결", id)

	return &dbConnection{id}, nil
}

func main() {
	var wg sync.WaitGroup
	wg.Add(maxGoroutines) //실행하고자하는 고루틴의 갯수를 카운터로 지정

	p, err := pool.New(createConnection(), pooledResources) //New 함수에 팩토리함수와, 관리하고다 하는 리소스의 갯수 전달
	if err != nil {
		log.Println(err)
	}

	for query := 0; query < maxGoroutines; query++ {
		go func(q int) { //각 고루틴에는 질의 값의 복사본을 전달해야 한다. 고루틴의 값들이 동일한 질의 값을 공유하지 않기 위해
			performQueries(q, p)
			wg.Done()
		}(query)
	}

	wg.Wait() //고루틴의 실행이 종료될 때까지 대기

	log.Println("Terminated")
	p.Close() //풀을 닫음
}

func performQueries(query int, p *pool.Pool) {
	conn, err := p.Acquire() //풀에서 데이터베이스 연결 리소스를 획득
	if err != nil {
		log.Println(err)
		return
	}

	defer p.Release(conn) //함수가 종료시 연결 리소스를 다시 되돌림

	time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
	log.Printf("질의 : QID[%d] CID[%d]\n", query, conn.(*dbConnection).ID)
}
