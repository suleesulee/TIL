var person = {} // object 빈 객체 만듬
person.name = 'su'; //객체안 변수 - 프로퍼티
person.introduce = function(){//객체안 함수 - 메소드
    return 'My name is '+ this.name; // this 함수가 담겨있는 객체를 뜻함
}
document.write(person.introduce());


var person = {
    'name' : 'su',
    'introduce' : function(){
        return 'My name is ' + this.name;
    }
}
document.write(person.introduce());


function Person() {}
var p = new Person();
p.name = 'su';
p.introduce = function(){
    return 'My name is' + this.name;
}
document.write(p.introduce()+"<br />");


function Person(name) {
    this.name = name;
    this.introduce = function(){
        return 'My name is '+ this.name; 
    }
}

//생성자는 그냥 함수.. 클래스에 존재하는게 아님(자바와 다름)