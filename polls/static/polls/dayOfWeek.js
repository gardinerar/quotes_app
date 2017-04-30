var date = new Date();
var dayNum = date.getDay();
var weekday;
function getWeekDay(dayNum) {
    switch(dayNum) {
        case 1:
            return "Monday";
        case 2: 
            return "Tuesday";
        case 3:
            return "Wednesday";
		case 4: 
            return "Thursday";
        case 5:
            return "Friday";
        case 6:
            return "Saturday";
        case 7:
            return "Sunday";
        default:
            return "Not a weekday";
	}
}
weekday = getWeekDay(dayNum);
var text = document.createTextNode(weekday);
var element = document.getElementById("h3");
element.innerHTML = weekday + "'s " + element.innerHTML;