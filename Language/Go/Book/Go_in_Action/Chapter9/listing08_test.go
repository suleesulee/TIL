package listing08

import(
	"net/http"
	"testing"
)

const checkMark = "\u2713"
const ballotX = "\u2717"

func TestDownload(t *testing.T){
	var urls= []struct{
		url string
		statusCode int
	}{
		{
			"http://www.goinggo.net/feeds/posts/default?alt=rss",
			http.StatusOK,
		},
		{
			"http://rss.cnn.com/rss/cnn_topstbadurl.rss",
			http.StatusNotFound,
		},
	}

	t.Log("각각 다른 콘텐츠에 대한 다운로드 확인")
	{
		for _, u := range urls {
			t.Logf("\tURL \"%s\" 호출시 상태코드가 \"%d\"인지 확인.", u.url, u.statusCode)		
			{
				resp, err := http.Get(u.url)
				if err != nil{
					t.Fatal("\t\tHTTP GET 요청을 보냈는지 확인", ballotX, err)
				}
				t.Log("\t\tHTTp GET요청을 보냈는지 확인", checkMark)

				defer resp.Body.Close()
				
				if resp.StatusCode == u.statusCode {
					t.Logf("\t\t상태코드가 \"%d\"인지 확인 %v", u.statusCode, checkMark)
				} else {
					t.Errorf("\t\t상태코드가 \"%d\"인지 확인 %v %v", u.statusCode, ballotX, resp.StatusCode)
				}

			}
		
		}
	}
}