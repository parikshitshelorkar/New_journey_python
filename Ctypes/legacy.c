// legacy.c
#include <stdio.h>
#include <stdlib.h>

void increment(int *value)
{
    (*value)++;
}


void process(int *input, int *output, int size)
{
    for (int i = 0; i < size; i++)
    {
        output[i] = input[i] * 2;
    }
}

// struct *-----------------------
typedef struct{
    int id;
    float salary;

} Employee;

void increase_salary(Employee *employee){
    employee->salary += 5000;
}

// char *----------------------
void uppercase(char *text){
    for(int i=0; text[i]!='\0'; i++){
        if(text[i] >= 'a' && text[i]<='z')
        {
            text[i] = text[i]-32;
        }
    }
}

//Pointer-to-pointer-------------
void create_number(int **value){
    //pointer to an int pointer 
    *value = (int*)malloc(sizeof(int));
    **value =100;
}

//memory ownership----------------------
char* get_name()
{
    char *name = malloc(100);
    strcpy(name, "Ravi");
    return name;
}

void free_memory(char *ptr){
    free(ptr);
}
