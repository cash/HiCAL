#include "utils.h"

#include <ctime>
#include <iostream>

void msg(const char *message){
    fprintf(stderr, "%s", message);
    fprintf(stderr, "\n");
}

void fail(const char *message, int e){
    msg(message);
    exit(e);
}

void msg(const std::string &str){
    msg(str.c_str());
}

void fail(const std::string &str, int e){
    fail(str.c_str(), e);
}

void bmi_log(const std::string &str){
    time_t rawtime;
    char buffer[80];

    time(&rawtime);
    tm *curtime = localtime(&rawtime);
    strftime(buffer, sizeof(buffer), "%m-%d-%Y %H:%M:%S", curtime);
    std::cerr << buffer << " - " << str << std::endl;
}

void bmi_log_timer(const std::string &key, int ms){
    bmi_log("Time (" + key + "): " + std::to_string(ms) + " ms");
}
