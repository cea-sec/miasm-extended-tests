#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


/* 32 bits */
int test_s32_pos_or_equal(int32_t a)
{
	if (a >= 0)
		return 1;
	return 0;
}

int test_s32_neg(int32_t a)
{
	if (a < 0)
		return 1;
	return 0;
}

int test_s32_greater(int32_t a, int32_t b)
{
	if (a > b)
		return 1;
	return 0;
}

int test_s32_greater_or_equal(int32_t a, int32_t b)
{
	if (a >= b)
		return 1;
	return 0;
}


int test_s32_lesser(int32_t a, int32_t b)
{
	if (a < b)
		return 1;
	return 0;
}

int test_s32_lesser_or_equal(int32_t a, int32_t b)
{
	if (a <= b)
		return 1;
	return 0;
}

int test_u32_greater(uint32_t a, uint32_t b)
{
	if (a > b)
		return 1;
	return 0;
}

int test_u32_greater_or_equal(uint32_t a, uint32_t b)
{
	if (a >= b)
		return 1;
	return 0;
}

int test_u32_lesser(uint32_t a, uint32_t b)
{
	if (a < b)
		return 1;
	return 0;
}

int test_u32_lesser_or_equal(uint32_t a, uint32_t b)
{
	if (a <= b)
		return 1;
	return 0;
}



/* 64 bits */


int test_s64_pos(int64_t a)
{
	if (a >= 0)
		return 1;
	return 0;
}

int test_s64_neg(int64_t a)
{
	if (a < 0)
		return 1;
	return 0;
}

int test_s64_greater(int64_t a, int64_t b)
{
	if (a > b)
		return 1;
	return 0;
}


int test_s64_greater_or_equal(int64_t a, int64_t b)
{
	if (a >= b)
		return 1;
	return 0;
}

int test_s64_lesser(int64_t a, int64_t b)
{
	if (a < b)
		return 1;
	return 0;
}

int test_s64_lesser_or_equal(int64_t a, int64_t b)
{
	if (a <= b)
		return 1;
	return 0;
}





int test_u64_greater(uint64_t a, uint64_t b)
{
	if (a > b)
		return 1;
	return 0;
}


int test_u64_greater_or_equal(uint64_t a, uint64_t b)
{
	if (a >= b)
		return 1;
	return 0;
}

int test_u64_lesser(uint64_t a, uint64_t b)
{
	if (a < b)
		return 1;
	return 0;
}

int test_u64_lesser_or_equal(uint64_t a, uint64_t b)
{
	if (a <= b)
		return 1;
	return 0;
}


/* f32 */

int test_float_pos_or_equal(float a)
{
	if (a >= 0.0)
		return 1;
	return 0;
}

int test_float_neg(float a)
{
	if (a < 0.0)
		return 1;
	return 0;
}

int test_float_greater(float a, float b)
{
	if (a > b)
		return 1;
	return 0;
}


int test_float_greater_or_equal(float a, float b)
{
	if (a >= b)
		return 1;
	return 0;
}


int test_float_lesser(float a, float b)
{
	if (a < b)
		return 1;
	return 0;
}


int test_float_lesser_or_equal(float a, float b)
{
	if (a <= b)
		return 1;
	return 0;
}




/* double */

int test_double_pos_or_equal(double a)
{
	if (a >= 0.0)
		return 1;
	return 0;
}

int test_double_neg(double a)
{
	if (a < 0.0)
		return 1;
	return 0;
}

int test_double_greater(double a, double b)
{
	if (a > b)
		return 1;
	return 0;
}


int test_double_greater_or_equal(double a, double b)
{
	if (a >= b)
		return 1;
	return 0;
}


int test_double_lesser(double a, double b)
{
	if (a < b)
		return 1;
	return 0;
}


int test_double_lesser_or_equal(double a, double b)
{
	if (a <= b)
		return 1;
	return 0;
}








int main()
{
	int ret;
	volatile int32_t int32_a;
	volatile int32_t int32_b;

	volatile uint32_t uint32_a;
	volatile uint32_t uint32_b;

	volatile int64_t int64_a;
	volatile int64_t int64_b;

	volatile uint64_t uint64_a;
	volatile uint64_t uint64_b;

	volatile float float_a;
	volatile float float_b;

	volatile double double_a;
	volatile double double_b;

	int32_a = 0;
	int32_b = 0x10;


	uint32_a = 0;
	uint32_b = 0x10;

	int64_a = 0;
	int64_b = 0x10;

	uint64_a = 0;
	uint64_b = 0x10;

	/* signed */
	ret = test_s32_pos_or_equal(int32_a);
	printf("ret: %d\n", ret);
	ret = test_s32_neg(int32_a);
	printf("ret: %d\n", ret);

	ret = test_s32_greater(int32_a, int32_b);
	printf("ret: %d\n", ret);
	ret = test_s32_greater_or_equal(int32_a, int32_b);
	printf("ret: %d\n", ret);

	ret = test_s32_lesser(int32_a, int32_b);
	printf("ret: %d\n", ret);
	ret = test_s32_lesser_or_equal(int32_a, int32_b);
	printf("ret: %d\n", ret);

	/* unsigned */
	ret = test_u32_greater(uint32_a, uint32_b);
	printf("ret: %d\n", ret);
	ret = test_u32_greater_or_equal(uint32_a, uint32_b);
	printf("ret: %d\n", ret);

	ret = test_u32_lesser(uint32_a, uint32_b);
	printf("ret: %d\n", ret);
	ret = test_u32_lesser_or_equal(uint32_a, uint32_b);
	printf("ret: %d\n", ret);


	/* signed 64*/
	ret = test_s64_pos(int64_a);
	printf("ret: %d\n", ret);
	ret = test_s64_neg(int64_a);
	printf("ret: %d\n", ret);

	ret = test_s64_greater(int64_a, int64_b);
	printf("ret: %d\n", ret);

	ret = test_s64_greater_or_equal(int64_a, int64_b);
	printf("ret: %d\n", ret);

	ret = test_s64_lesser(int64_a, int64_b);
	printf("ret: %d\n", ret);

	ret = test_s64_lesser_or_equal(int64_a, int64_b);
	printf("ret: %d\n", ret);


	/* unsigned 64*/

	ret = test_u64_greater(uint64_a, uint64_b);
	printf("ret: %d\n", ret);

	ret = test_u64_greater_or_equal(uint64_a, uint64_b);
	printf("ret: %d\n", ret);

	ret = test_u64_lesser(uint64_a, uint64_b);
	printf("ret: %d\n", ret);

	ret = test_u64_lesser_or_equal(uint64_a, uint64_b);
	printf("ret: %d\n", ret);


	/* float */

	ret = test_float_pos_or_equal(float_a);
	printf("ret: %d\n", ret);

	ret = test_float_neg(float_a);
	printf("ret: %d\n", ret);

	ret = test_float_greater(float_a, float_b);
	printf("ret: %d\n", ret);

	ret = test_float_greater_or_equal(float_a, float_b);
	printf("ret: %d\n", ret);

	ret = test_float_lesser(float_a, float_b);
	printf("ret: %d\n", ret);

	ret = test_float_lesser_or_equal(float_a, float_b);
	printf("ret: %d\n", ret);



	/* double */

	ret = test_double_pos_or_equal(double_a);
	printf("ret: %d\n", ret);

	ret = test_double_neg(double_a);
	printf("ret: %d\n", ret);

	ret = test_double_greater(double_a, double_b);
	printf("ret: %d\n", ret);

	ret = test_double_greater_or_equal(double_a, double_b);
	printf("ret: %d\n", ret);

	ret = test_double_lesser(double_a, double_b);
	printf("ret: %d\n", ret);

	ret = test_double_lesser_or_equal(double_a, double_b);
	printf("ret: %d\n", ret);



	return 0;
}
