class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [nums[0]]
        revProducts = [nums[-1]]
        print(revProducts)
        for n in nums[1:]:
            products.append(n*products[-1])
        for n in nums[:-1:][::-1]:
            revProducts.insert(0,n*revProducts[0])

        products.insert(0,1)
        revProducts.insert(0,1)
        products.append(1)
        revProducts.append(1)
        print(products)
        print(revProducts)
        allProducts = []
        for i in range(1, len(products)-1):
            allProducts.append(products[i-1]*revProducts[i+1])
        return allProducts

