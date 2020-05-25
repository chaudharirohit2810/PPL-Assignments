#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
// #include<windows.h>

// Structure for clock timer
typedef struct
{
    int seconds;
    int minutes;
    int hours;
} Clock;

// Increment hours
void *hours_inc(void* clockObj) {
    Clock* new_clock = clockObj;
    
    while (1)
    {
        sleep(60 * 60);
        new_clock->hours = new_clock->hours + 1;
        // printf("%d\n", new_clock->hours);
        new_clock->minutes = 0;
        // new_clock->seconds = 0;
    }

}

// Increment minutes
void *minutes_inc(void* clockObj) {
    Clock* new_clock = clockObj;
    
    while (1)
    {
        sleep(60);
        new_clock->minutes = new_clock->minutes + 1;
        // printf("%d\n", new_clock->minutes);
        new_clock->seconds = 0;
    }

}

// Increment Seconds
void *seconds_inc(void* clockObj) {
    Clock* new_clock = clockObj;
    
    while (1)
    {
        sleep(1);
        new_clock->seconds = new_clock->seconds + 1;
        // printf("%d\n", new_clock->seconds);
    }

}

void* clock_fun(void* clockObj) {

    Clock* new_clock = clockObj;

    char hrs[3] = {'\0'};
    char minutes[3] = {'\0'};
    char seconds[3] = {'\0'};
    
    while (1)
    {
        if(new_clock->hours < 10) {
            sprintf(hrs, "0%d", new_clock->hours);
        }else {
            sprintf(hrs, "%d", new_clock->hours);
        }

        if(new_clock->minutes < 10) {
            sprintf(minutes, "0%d", new_clock->minutes);
        }else {
            sprintf(minutes, "%d", new_clock->minutes);
        }

        if(new_clock->seconds < 10) {
            sprintf(seconds, "0%d", new_clock->seconds);
        }else {
            sprintf(seconds, "%d", new_clock->seconds);
        }
        

        printf("\r%s:%s:%s", hrs, minutes, seconds);

        
    }

    
    
}



int main() {
    printf("Clock: \n");

    // Initializing object
    Clock* seconds = malloc(sizeof(clock));
    seconds->seconds = 0;
    seconds->hours = 00;
    seconds->minutes = 0;


    // Thread objects
    pthread_t thread1, thread2, thread3, thread4;

    //Creating threads
    pthread_create(&thread1, NULL, seconds_inc, seconds);
    pthread_create(&thread2, NULL, minutes_inc, seconds);
    pthread_create(&thread3, NULL, hours_inc, seconds);
    pthread_create(&thread4, NULL, clock_fun, seconds);

    //Joining threads
    int join1 = pthread_join(thread1, NULL);
    int join2 = pthread_join(thread2, NULL);
    int join3 = pthread_join(thread3, NULL);
    int join4 = pthread_join(thread3, NULL);

    

    printf("Clock ends!!\n");
}
