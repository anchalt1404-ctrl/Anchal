
#include <stdio.h>

int main()
{
    char name[50];
    int marks[5];
    int total = 0;
    float percentage;
    int i;
    int pass = 1;

    printf("================================\n");
    printf("     STUDENT RESULT SYSTEM\n");
    printf("================================\n");

    printf("Enter Student Name: ");
    scanf(" %[^\n]", name);

    printf("\nEnter marks of 5 subjects (out of 100):\n");

    for(i = 0; i < 5; i++)
    {
        printf("Subject %d: ", i + 1);
        scanf("%d", &marks[i]);

        if(marks[i] < 0 || marks[i] > 100)
        {
            printf("Invalid marks! Enter marks between 0 and 100.\n");
            return 1;
        }

        total = total + marks[i];

        if(marks[i] < 33)
        {
            pass = 0;
        }
    }

    percentage = total / 5.0;

    printf("\n================================\n");
    printf("          STUDENT RESULT\n");
    printf("================================\n");

    printf("Student Name: %s\n", name);
    printf("Total Marks: %d / 500\n", total);
    printf("Percentage: %.2f%%\n", percentage);

    if(pass == 1)
    {
        printf("Result: PASS\n");
    }
    else
    {
        printf("Result: FAIL\n");
    }

    printf("================================\n");

    return 0;
}
