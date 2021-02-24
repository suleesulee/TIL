//Chapter 5

/*
	5.1 사용자 정의 타입
   
	Go에서 사용자 정의 타입을 선언하는 방법은 크게 2가지
   1. struct
*/

type user struct {
	name      string
	email     string
	phone_num int
}

/*
   var로 선언하면 변수가 제로 값이라는 묵시적이라고 함
*/

var tom user

/*
   값을 줘서 초기화 하려면 구조체 리터럴을 사용해서 초기화
*/

elsa := user{
	name:      "Elsa",
	email:     "elsa@gmail.com",
	phone_num: 01011112222,
}

/*
아래 방법도 가능
*/
elsa2 := user{"Elsa", "else@gmail.com", 01011112222}

/*
	구조체 타입 내포
*/

type admin{
	person user
	level string
}

anna : admin{
	person: user{
		name:"anna",
		email: "anna@gmail.com",
		phone_num: 01011113333,
	},
	level: "super",
}

/*
	2. 방법 기존의 타입을 바탕으로 새로운 타입선언
*/
type Duration int64

/*
	int64는 기본형 
	Go에서는 int64와 Duration은 다른 타입 취금
*/

func main(){
	var dur Duration
	dur = int64(1000)
}

/*
	go의 컴파일러는 Duration이 int64를 기반 타입으로 파생되었다고 해도
	int64와 Duration은 다른 타입으로 보기때문에 해당 코드는 에러가 남
	묵시적 형변환을 하지 않음
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
