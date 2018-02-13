#include <Daisy.h>

/** 
 * This is being used to compared against an
 * unsigned long. Make sure to add an L behind
 * the constant.
 *
 * Hello World
 */
#define THRESHOLD 5L

Daisy daisy;

void setup() {
    // put your setup code here, to run once:
    daisy = Daisy(3,5);
    PRINTLN("Daisy has been initialized!")
}

/*void loop() {
    // put your main code here, to run repeatedly:
    unsigned long dist = daisy.leftPingIN();
    PRINTLN("%lu %lu", dist, THRESHOLD)
    if(dist <= THRESHOLD) {
      //PRINTLN("HALTING")
      daisy.halt();
    } else {
      daisy.forward(100);
    }*/

void loop(){

    unsigned long distR = daisy.rightPingIN();
    unsigned long distL = daisy.leftPingIN();
    
    if(distR <= 5){
      daisy.turn(CCW, 100)
    }
    if(distL <= 5){
      daisy.turn(CW, 100)
    }
    else{
       daisy.forward(100)
    }



}
