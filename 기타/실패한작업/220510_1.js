let json = JSON.stringify(["apple","banana"]);
console.log(json);

const rabbit = {
    name : 'tori',
    color: 'white',
    size: null,
    birthDay: new Date(),
    jump:()=>{
        console.log(`${name} can jump!`);
    },
};

json = JSON.stringify(rabbit);
console.log(json);

json = JSON.stringify(rabbit, ["name","color","birthDay"]);
console.log(json);

json = JSON.stringify(rabbit, (key,val))