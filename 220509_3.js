var x = '{"sessionDate":"2022-05-09T16:00.000Z"}';

//서로 같은건가보다.. eval()과 JSON.parse()
console.log(eval('(' + x + ')').sessionDate);
console.log(JSON.parse(x).sessionDate);


var y = '{"sessionDate":new Date()}';

// 자바스크립트 명령문인 new Date()가 포함되었는데, JSON.parse()함수에서 에러가 난다!
console.log(eval('(' + y + ')').sessionDate);
console.log(JSON.parse(y).sessionDate);

// 어쨋든 eval() 보다 JSON.parse()를 권한다는 얘기인데.. eval()은 보안문제 때문에 그렇다니~