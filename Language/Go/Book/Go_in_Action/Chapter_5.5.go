/* 210302 sulee */

////////////////////////
/*5.5 Type enbedding*/
////////////////////////

/*
기존 선언된 타입을 새로운 구조체 내부에 선언하는것
포함되는 타입은 외부타입의 내부타입으로 활용됨
내부타입에 선언된 식별자는 승격을 통해 외부 타입의 식별자로 승격 외부타입의 일부로 인식되어
외부 타입처럼 동작함
*/
package main

import "fmt"

type notifier interface {
	notify()
}

type user struct {
	name  string
	email string
}

func (u *user) notify() {
	fmt.Printf("사용자에게 메일을 전송: %s<%s>\n",
		u.name,
		u.email)
}

/*

//notify를 외부 타입에서 정의하면 내부 타입의 notify는 승격되지 않음

func (a *admin) notify() {
	fmt.Printf("관리자에게 메일을 전송: %s<%s>\n",
		a.name,
		a.email)
}
*/

type admin struct {
	user  //내부 타입
	level string
}

func main() {
	ad := admin{
		user: user{
			name:  "jane doe",
			email: "jane@gmail.com",
		},
		level: "super",
	}

	ad.user.notify()

	ad.notify() //ad에는 메소드가 없지만 내부타입의 승격을 통해 호출이 가능

	sendNotification(&ad) //내부 타입에 구현된 인터페이스가 승격을 통해 호출이 가능
}

func sendNotification(n notifier) {
	n.notify()
}
