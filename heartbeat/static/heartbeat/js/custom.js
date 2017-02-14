var heart_click_count = 0;
var my_start_time;
var my_stop_time;
function heart_click(){
    if (heart_click_count == 0){
        my_start_time = get_time();
        heart_click_count += 1;
    }
    else if(heart_click_count == 20){
        my_stop_time = get_time();
        total_time_ms = my_stop_time - my_start_time;
        total_time_s = total_time_ms/1000;
        total_time_m = total_time_s/60;
        bpm = heart_click_count/total_time_m;
        $('.output').text(bpm);
        console.log(bpm);
        heart_click_count = 0;
    }
    else{
        heart_click_count += 1;
    }
}
function get_time(){
    var d = Date.now();
    return d;
}

//function time_difference(start, stop){
//    start = start.split(" ")[0].split(":");
//    stop = stop.split(" ")[0].split(":");
//    start_h = start[0];
//    start_m = start[1];
//    start_s = start[2];
//
//    stop_h = stop[0];
//    stop_m = stop[1];
//    stop_s = stop[2];
//
//    console.log(stop_h-start_h);
//    console.log(stop_m-start_m);
//    console.log(stop_s-start_s);
//}