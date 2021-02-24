function Person(name){
    this.name = name;
}
Person.prototype.name = null;
Person.prototype.introduce = function(){
    return 'My name is' + this.name;
}
var p1 = new Person('su');
document.write(p1.introduce()+"<br/>");


///


function Person(name){
    this.name = name;
}
Person.prototype.name = null;
Person.prototype.introduce= function(){
    return 'My name is' + this.name;
}

function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
Programmer.prototype.coding = function(){
    return "hello world";
}

var p1 = new Programmer('su');
document.write(p1.introduce() + "<br/>");