package listing01


import(
	"net/http"
	"testing"
)
const checkMark = "\u2713"
const ballotX = "\u2717"

func TestDownload(t *testing.T){
	url := "http://www.goinggo.net/feeds/posts/default?alt=rss"
	statusCode:=200

	t.Log("contents download func test start")
	{
		t.Logf("\tURL \"%s\" 호출시 상태코드가 \"%d\"인지 확인.", url, statusCode)
	}

	resp,err := http.Get(url)
	if err != nil{
		t.Fatal("\t\tHTTP GET 요청을 보냈는지 확인", ballotX, err)
	}
	t.Log("\t\tHTTP GET 요청을 보냈는지 확인", checkMark)

	defer resp.Body.Close()

	if resp.StatusCode == statusCode{
		t.Logf("\t\t상태코드가 \"%d\" 인지 확인 %v", statusCode, checkMark)
	} else{
		t.Errorf("\t\t 상태코드가 \"%d\" 인지 확인 %v %v", statusCode, ballotX, resp.StatusCode)
	}
}