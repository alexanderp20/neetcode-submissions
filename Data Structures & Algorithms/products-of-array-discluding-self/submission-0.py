class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        postfix_product = [1]
        product = []
        for i in range(len(nums)):
            if i != 0:
                prefix_product.append(prefix_product[i-1] * nums[i - 1])
            # print(prefix_product)

        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                postfix_product.append(postfix_product[len(postfix_product) - 1] * nums[i + 1])
            # print(postfix_product)
        postfix_product.reverse()

        for i in range(len(nums)):
            product.append(prefix_product[i] * postfix_product[i])

        return product

            