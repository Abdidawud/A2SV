class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]
        kelvin=celsius + 273.15
        f=celsius *1.80 +32.00
        ans.append(kelvin)
        ans.append(f)
        return ans