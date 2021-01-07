#ifndef UTILS_H
#define UTILS_H

#include <string>
#include <chrono>


#define TIMER_BEGIN(key) \
    auto start##key = std::chrono::steady_clock::now();

#define TIMER_END(key) \
    bmi_log_timer(#key, (std::chrono::duration_cast<std::chrono::milliseconds> (std::chrono::steady_clock::now() - start##key)).count());

void msg(const char *message);
void fail(const char *message, int e);
void msg(const std::string &str);
void fail(const std::string &str, int e);
void bmi_log(const std::string &str);
void bmi_log_timer(const std::string &key, int ms);
#endif // UTILS_H
