/*
Chapter 7
동시성 패턴
*/

/*
세 가지 동시성 패턴을 구현해 봄
7.1 Runner Package
runner 패키지의 목적은 채널을 이용해 프로그램의 실행 시간을 관창하고 프로그램이 너무 오래 실행되면 프로그램을 종료 하는 것
백그라운드 작업 프로세스를 예약 실행하는 프로그램을 작성할 때 유용한 기법
크론작업(cron job), iron.io 같은 작업자 기반 클라우드 환경에서 동작하는 프로그램일 수 있음
*/

package main

import (
	"errors"
	"os"
	"os/signal"
	"time"
)

type Runner struct {
	interrupt chan os.Signal

	complete chan error

	timeout <-chan time.Time

	tasks []func(int)
}

var ErrTimeout = errors.New("시간 초과")

var ErrInterrupt = errors.New("운영체제 인터럽트 수신")

func New(d time.Duration) *Runner {
	return &Runner{
		interrupt: make(chan os.Signal, 1),
		complete:  make(chan error),
		timeout:   time.After(d),
	}
}

func (r *Runner) Add(tasks ...func(int)) {
	r.tasks = append(r.tasks, tasks...)
}

func (r *Runner) Start() error {
	signal.Notify(r.interrupt, os.Interrupt)

	go func() {
		r.complete <- r.run()
	}()

	select {
	case err := <-r.complete:
		return err

	case <-r.timeout:
		return ErrTimeout
	}
}

func (r *Runner) run() error {
	for id, task := range r.tasks {
		if r.gotInterrupt() {
			return ErrInterrupt
		}

		task(id)
	}
	return nil
}

func (r *Runner) gotInterrupt() bool {
	select {
	case <-r.interrupt:
		signal.Stop(r.interrupt)
		return true

	default:
		return false
	}
}

/*

 */
/**/
/**/
/**/
/**/
/**/
/**/
/**/
/**/
/**/
/**/
/**/
