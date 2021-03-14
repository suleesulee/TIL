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

const {
	Ldate = 1 << iota   // 1<<0 00000001
	Ltime = 			// 1<<1 00000010
	Lmicroseconds		// 1<<2 00000100
	....
}


비트연산으로 왼쪽으로 이동.
독자적인 플래그로써 동작할수있게함

LstdFlags = Ldate(1) | Ltime(2) = 00000011 = 3

LstdFlags를 정의하면 iota 체인의 사용은 중단됨


log.SetFlags(log.Ldate |log. Lmicroseconds | log.Llongfile)

형식화 하는 버전은
ln 대신 f 붙은 함수이름

고루틴 간에도 안전하게 활용가능
여러 고루틴이 동일 로거에서 함수를 동시에 호출해도 간섭이 발생하지 않음
*/

/*
사용자정의 로거도 생성가능하다
Logger타입을 직접 생성해야 하고
출력장치, 접두어, 플래그를 성정해줘야함
*/

var (
	Trace   *log.Logger
	Info    *log.Logger
	Warning *log.Logger
	Error   *log.Logger
)

//로거의 중요도에 따라 다르게 설정

Trace = log.New(ioutil.Discard, "Trace: ", log.Ldate | log.Ltime | log.Lshortfile)
Error = log.New(os.Stdout, "Error:" ,  log.Ldate)
//log 패키지의 New 함수를 호출

//원형
func New(out io.Writer, prefix string, flag int) *Logger {
	return &Logger{out: out, prefix: prefix, flag: flag}
}

//log는 표준 라이브러리를 사용하라 고퍼들 대부분이 사용한다


/*
인코딩 디코딩

XML보다 JSON으로 데이터를 다루는 것이 요즘 트렌드
더 적은 마크업을 사용하기 때문에 적은 양의 데이터로 동일 내용을 표현 가능함
*/


type (
	gResult struct {
		URL string 'json:"url"'
		Title string 'json:"title"'
		Content string 'json:"content"'
		....
	}
	
	gRespose struct{
		ResData struct{
			Res []gResult 'json:"results'
		} 'json:"responseData'
	}
)

'json:"ex"'
//태그라고 함 JSON문서와 구조체 타입 간의 필드 매핑을 위한 메타데이터

var gr gRespose
err = json.NewDecoder(resp.Body).Decode(&gr)

fmt.Print(gr)




func NewDecoder (r io.Reader) *Decoder
//Decoder 타입의 포인터를 리턴

func (dec *Decoder) Decode(v interface{}) error
//빈 인터페이스는 모든 타입이 구현하는 인터페이스 어떠한 타입이라도 받아들일 수 있음
//Decode 메서드는 리플렉션을 통해 파라메타의 정보를 파악해서 지정된 타입으로 디코딩 해줌

//JSON문서의 문자열 값은 문자열 바이트 슬라이스로 변환후 json 패키지의 Unmarshal함수를 사용

var JSON_EX = '{ "test": "mar", "test2": "shal", "test3": {"tt": "aa", "dd" : "ee"}}'

func ex(){	
	var m MarEx
	//var m map[string]interface{}
	err := json.Unmarshal([]byre(JSON_EX), &m)
	if err != nil {
		...s
	}
}


//fmt.Println("test3:", m["test3"].(map[string]interface{})["tt"])
//위와 같이 맵을 이용해서 디코딩도 가능하다

m := make(map[string]interface{})
/*
{key: string, value: 모든타입}으로 구성된 map
*/

data, err := json.MarshalIndent(m, "", "   ")
if err != nil {
	log.Println("err", err)
	return
}

func MarshalIndent(v interface{}, prefix, indent string)([]byte, error){....}

//해당 함수는 빈 인터페이스를 사용라며 리플렉션을 통해 맵타입 JSON 문자열로 변환



//GO에서 JSON, XML을 사용할땐 표준라이브러리를 쓰자
//매우 잘 구현되어있으며 속도도 빠르다.

/**/
/*
UNIX 기반 운영체제는 한프로그램의 출력을 다른프로그램의 입력으로 사용가능

go는 io.Writer, io.Reader 인터페이스가 제공하는 추상화덕분에 
io패키지에 구성된 함수와 메서드는 데이터의 타입, 읽고 쓰는 방법에 신경을 쓰지 않음

type Writer interface{
	Write(p []byte) (n int, err error)
}

전달된 바이트 슬라이스의 전체를 출력해야함
작업에 실패하면 반드시 에러 리턴
출력된 바이트의 길이는 슬라이스의 길이보다 작을 수 있지만 더 많아서는 안됨
*/

/*
type Reader interface{
	Read(p []byte) (n int, err error)
}

첫번쨰 리턴값은 읽어들인 바이트의 길이
두번째는 에러값

읽은 바이트가 0일때 nil 리턴 금지
아무것도 하지 않은 상황으로 간주해야함
*/
/*
표준라이브러리를 잘 관찰하면 Go 디자이너들이 패키지와 API를 작성하는 방식 또한 이해가능

*/
/**/
/**/
/**/
/**/
/**/
