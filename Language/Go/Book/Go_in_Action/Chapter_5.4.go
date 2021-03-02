/* 210302 sulee */

////////////////////////
/*5.4 Interface*/
////////////////////////

/*
어떤 타입이 인터페이스를 구현하면 그 타입의 값을 통해 그 기능을 외부에 노출 가능
인터페이스를 선언하고 구현하려면 높은 수준의 go의 기술적 기반이 필요
*/

//ex 1
/*
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"

	"github.com/labstack/gommon/email"
)

func init() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./x <url>")
		os.Exit(-1)
	}
}

func main() {
	r, err := http.Get(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}

	io.Copy(os.Stdout, r.Body)
	if err := r.Body.Close(); err != nil {
		fmt.Println(err)
	}
}

*/
/* http의 Get함수를 통해 http.req를 리턴 받음
http.Request타입은 io.ReadCloser 인터페이스 타입의 Body 필드를 제공
io.Copy 함수의 두번째 매개변수로 전달되는데 io.Copy 두번째 매개변수는 io.Reader 인터페이스 타입임
io.Copy 함수의 첫번째 매개변수는 데이터를 기록할 목적지 예제에서는 stdout이라는 인터페이스 값

결과적으로 웹서버의 request 스트림을 stdout(모니터)에 출력함
*/

//ex 2
/*
package main

import {
	"bytes"
	"io"
	"fmt"
	"os"
}

func main(){
	var b byte.Buffer

	b.Write([]byte("Hi"))

	fmt.Fprintf(&b, "Go in action")

	io.Copy(os.stdout, &b)
}
*/

/* 버퍼에 문자열 기록 Fprintf 함수로 문자열 덧붙임 버퍼 내용을 출력
byte.Buffer 타입의 포인터는 io.Reader의 인터페이스도 구현하기에 io.Copy가 stdout에 출력가능함
*/

/*인터페이스는 단지 행위를 선언하기 위한 타입으로 사용자 정의 타입이 인터페이스를 구현해야함
사용자 정의 타입을 종종 구현타입(concrete type)이라고 부름
인터페이스 타입 값에 선언된 메서드를 호출하면 사용자정의 타입에 구현된 동일한 메서드가 실행됨
인터페이스 값은 두 개의 워드(word)로 구성된 데이터 구조
첫번째 워드는 iTable이라는 내부 테이블에 대한 포인터를 가지고 있음
iTable은 저장된 값의 타입과 그 값에 관련된 메서드 목록을 가지고 있음
두번째 워드는 저장된 값에 대한 포인터

메서드 집합은 인터페이스를 준수하는 것과 관련된 규칙 정의
*/
/*
package main

import "fmt"

type notifier interface {
	nortify()
}

type user struct{
	name string
	email string
}

func (u *user) notify(){
	fmt.Printf("사용자 메일 전송 %s<%s>\n",
		u.name,
		u.email)
}

func main() {
	u := user {"none", "none@email.com"}

	sendNotification(u)	//근데 이건 compile err 발생
	sendNotification(&u) 	//주소를 전달하면 괜찮음, 경우에 따라서는 값의 주소를 알아 낼수 없기 떄문
}

func sendNotification(n notifier){//notifier 인터페이스 매개변수 선언, notifier 인터페이스를 구현하는 값이라면 sendNotification 함수에 전달 가능
	n.notify()
}
*/
/*

값				메서드 수신자
=============================
V				(v V)
*V				(v V) 와 (v *V)

메서드 수신자			값
=============================
(v V)				v, *v
(v *V)				*v

값에 대한 메서드 집합은 오로지 값 수신자에 구현된 메서드만을 가짐

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
	fmt.Printf("사용자 메일 전송 %s<%s>\n",
		u.name,
		u.email)
}

type admin struct {
	name  string
	email string
}

func (a *admin) notify() {
	fmt.Printf("관리자 메일 전송 %s<%s>\n",
		a.name,
		a.email)
}

func main() {
	none := user{"none", "none@mail.com"}
	sendNotification(&none)
	ad := admin{"super", "super@admin.com"}
	sendNotification(&ad)
}

func sendNotification(n notifier) {
	n.notify()
}

/*
두개의 구현 타입이 notifier 인터페이스를 구현
어떤 구현 타입이든 인터페이스를 구현한다면 구현 타입의 종류와 관계없이 해당 메서드를 호출 할 수 있음
이를 통해 다형성의 특징을 가지게 됨
*/
