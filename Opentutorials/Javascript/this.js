var o = {
    func : function(){
        if(o === this){
            document.wirtie("o === this")
        }
    }
}


///

var funcTihs = null;

function Func(){
    funcTihs = this;
}

var o1 = Func();
if(funcThis === window){
    document.write('window</br>')
}

var o2 = new Func();
if(funcThis === o2){
    document.write('o2</br>')
}


///

var o = {}
var p = {}
function func(){
    switch(this){
        case o:
            document.write('o<br />');
            break;
        case p:
            document.write('p<br />');
            break;
        case window:
            document.write('window<br />');
            break;
    }
}

func();
func.apply(o);
func.apply(p);