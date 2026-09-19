#include <stdio.h>

#include "obd2/obd2.h"

int main(void)
{
    if (obd2_init() != 0)
    {
        fprintf(stderr, "Failed to initialize OBD2\n");
        return 1;
    }

    printf("OBD2 initialized successfully\n");

    return 0;
}