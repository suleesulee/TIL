//map initialize

dict1 := make(map[string]int) //key string type value int type
dict2 := map[string]string{"a": "1", "b": "2"}

/*
slice는 map의 value로는 사용가능
dict3 := map[int][]string

선언하기만 하면 nil map이 생성되는데 키와 값을 저장할 수 없다.

var map1 map[int]string //key, value 저장 불가


// map 내부의 key, value가 있는지 검사하는 법
//key 확인
value, exists := map1["a"]
//value 확인
if exists {
	fmt.Println(value)
}


value := map1["a"]
if value != "" {
	fmt.Println(value)
}

맵에 인덱스를 이용해 접근시 키가 존재 하지않더라도 항상 값 리턴된다.
키 타입의 제로 값 리턴
*/

/*
range를 이용한 key, value 값 추출
*/
map2 := map[string]string {
	"1" : "a"
	"2" : "b"
	"3" : "c"
}

for key, value := range map2{
	fmt.Println("key: %s, value: %s\n", key, value)
}

/*
delete를 이용한 키와 밸류의 삭제
*/

delete(map2, "1")


/*
맵은 함수에 전달하면 참조형으로 전달됨
*/
remove_ex(map2, "2")

func remove_ex(ex map[string]string, key string){
	delete(ex, key)
}

/*
슬라이스는 용량의 제한을 가지고 있지만 append를 통해 확장가능
맵은 용량이 정해져있지 않음
len을 통해 슬라이스, 맵의 길이를 알수있음
cap은 슬라이스에서만 

*/
/*

*/
/*

*/
/*

*/
/*

*/
/*

*/
/*

*/
