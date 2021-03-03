/* 210303 sulee */

////////////////////////
/*5.6 외부 노출 식별자와 비노출 식별자*/
////////////////////////

/*
Go는 패키지에 선언한 식별자를 외부에 노출하거나 숨기는 것을 지원
패키지 외부의 코드로부터 식별자들을 내부로 숨기는 것 (Incapsulation)
비노출 식별자라고함(unexporting identifier)
*/

/*
package counters

type alertCounter int
*/

package main

import "fmt"

func main() {
	counter := counters.alertCounter(10)

	fmt.Printf("counters : %d\n", counter)
}

/*
	*패키지의 이름과 코드를 저장할 폴더의 이름을 동일하게 사용
	식별자의 이름을 소문자로하면 외부에 노출되지 않는다.
	alertCounter는 int타입을 기반으로 하는 타입
	위의 코드는 실행이 안된다 alertCounter가 비노출타입이기 떄문에
	첫번째 글자를 대문자로 변경하면 접근할 수 있다
*/

/*
conters/counter.go

package counters

type alertCounter int

func New(value int) alertCounter{
	return alertCounter(value)
}


package main

import {
	"fmt"
	...
}

func main() {
	counter := counters.New(10)
	fmt.Printf("Counter: %d\n", counter)
}

*/

/*팩토리 함수에 New라는 이름을 지정하는 것도 Go의 규칙*/
alertCounter식별자는 비노출 식별자지만 New를 통해서 main함수는 이값에 접근하여 변수를 생성할 수있다.

package entities

type User struct {
	Name string
	email string
}

package main

import {
	"fmt"
	"..."
}

func main(){
	u := entities.User{
		Name: "none",
		email: "none@no.com",
	}

	fmt.Printf("사용자 %v\n", u)
}


email은 비노출 식별자이므로 오류가 발생한다

package entities
type user struct {
	Name string
	Email string
}

type Admin struct{
	user
	Rights int
}

package main

import {
	"fmt"
	".../entities"
}

func main(){
	a := entities.Admin{
		Rights: 10,
	}
}

a.Name = "none"
a.Email = "no@nomail.com"

fmt.Printf("사용자: %v\n", a)

외부로 노출이 불가능한 user타입을 포함하고있다.
내부타입이 비노출 타입이라 하더라도 내부 타입에 선언된 필드들은 외부로 노출 가능함
내부타입의 식별자들은 외부 타입으로 승격되지 때문에 내부타입에 선언된 식별자들은 외부타입의 값을 통해 접근가능

외부타입인 a를 통해 비노출 내부타입의 Name, Email에 접근하여 초기화 가능 user타입은 비노툴 타입이기 때문에 직접 접근은 불가