#include <stdio.h>
#include <string.h>
#include <cpuid.h>
#include <windows.h>

char* get_vendor(void){
    unsigned int eax, ebx, ecx, edx;
    static char vendor_string[13];
    if (!__get_cpuid(0, &eax, &ebx, &ecx, &edx)){
        return NULL;
    }
    memcpy(vendor_string, &ebx, 4);
    memcpy(vendor_string + 4, &edx, 4);
    memcpy(vendor_string + 8, &ecx, 4);
    vendor_string[12] = '\0';
    return vendor_string;
}

int main(void){
    char* vendor_string = get_vendor();
    SYSTEM_INFO sysInf;
    GetSystemInfo(&sysInf);
    printf("Logical: %u Threads\n", sysInf.dwNumberOfProcessors);
    printf("Processor (vendor): %s\n", vendor_string);
    return 0;
}