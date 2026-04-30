var d = new Date();
s = d.toISOString();
console.log(s[1]);

var d = new Date("2022-03-25");

console.log(d);

var d = new Date();



let year = d.getFullYear();
let month = d.getMonth();
let day = d.getDay();
let hour = d.getHours();
let minute = d.getMinutes();
let sec = d.getSeconds();

let diff = d.getTimezoneOffset();

console.log(year, month,day, hour, minute,sec , diff);

let UtcYear = d.getUTCFullYear();
let UtcMonth = d.getUTCMonth();
let UtcDay = d.getUTCDay();
let UtcHour = d.getUTCHours();
let UtcMinute = d.getUTCMinutes();
let UtcSec = d.getUTCSeconds();



console.log(UtcYear, UtcMonth,UtcDay,
    UtcHour, UtcMinute, UtcSec );