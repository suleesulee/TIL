/*
표준라이브러리

하위호환성을 보장한다
Go의 개발, 빌드 릴리즈 프로세서의 일부로 활용됨
컨트리뷰터들의 지속적인 관리
새로운 버전이 릴리즈될 때마다 테스트와 벤치마크를 진행해줌

표준라이브러리의 사용을 적극권장
코드를 더 쉽게 관리, 안정성 보장

Go는 다른 언어보다 표준 라이브러리에 대한 의존도가 높다
전통적인 표준라이브러리보다 더 많은 기능을 제공하기 때문이다.
네트워킹, HTTP, 암호화, 이미지 프로세싱 등...

$GOROOT/src/pkg 폴더에 표준라이브러리의 소스코드가 있다
이렇게 로컬에 저장해 놓는것은 GO 도구들이 동작하는데 중요한 요소로 작용한다
godoc, gocode, go build 까지도 이 소스를 로드한다.
*/

/*
로깅
Go의 표준라이브러리는 로그패키지를 지원함
로그를 위한 정보를 기록할 때는 다른 출력장치에 기록해야 프로그램의 결과와 로그가 뒤섞이는 일을 방지할수 있다.
이문제를 해결하기 위해 UNIX 아키텍트들은 stderr을 추가함
출력과 로그를 분리해냄 stdout, stderr
*/

package main

import "log"

//init 함수는 main 함수보다 먼저 호출됨
//시작과 동시에 log 패키지를 사용할 수 있도록 하는 것이 일반적이다.

func init() {
	log.SetPrefix("Trace")
	log.SetFlags(log.Ldate | log.Lmicroseconds | log.Llongfile)
}

func main() {
	log.Println("MSG")
	//Println을 호출 후 os.Exit(1)을 호출
	log.Fatalln("Critical Err MSG")
	//Println을 호출 후 panic함수를 호출
	log.Panicln("Panic MSG")
}

/*
const(
//비트 OR을 이용해 출력 항목을 조정

Ldate = 1<<iota
//날짜 : YYYY/MM/DD

Ltime
//시간: HH:MM:SS

Lmicroseconds
//마이크로초 부분 표시

Llongfile
//전체 파일 이름 및 줄번호 /a/b/c/d.go:11

Lshortfile
//Llogfile 플래그를 덮어씀 d.go:11

LstdFlags = Ldate | Ltime
//표준 로거를 위한 기본 값

)

*/
/*
iota 키워드는 상수 블록을 선언할 때 사용하는 특별한 키워드
코드 블록의 끝에 도달하거나 대입 구문이 발견될 때까지 동일한 표현식을 매 상수마다 중복해서 적용할 것을 컴파일러에 지시
iota 키워드의 기본 값을 0으로 하되 상수를 정의할 떄마다 1씩 증가시킴

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
