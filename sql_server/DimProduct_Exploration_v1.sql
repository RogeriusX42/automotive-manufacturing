USE AdventureWorksDW2020; 

-- SELECT * FROM DimProduct; 

SELECT 
	ProductKey, ProductAlternateKey, 
	EnglishProductName, SpanishProductName, FrenchProductName, 
	StandardCost, Color, SafetyStockLevel, ReorderPoint, ListPrice, Size, Weight, 
	DaysToManufacture, ProductLine, DealerPrice, Class, Style, 
	ModelName, LargePhoto, 
	EnglishDescription, FrenchDescription, ChineseDescription, ArabicDescription, ThaiDescription, GermanDescription, JapaneseDescription, TurkishDescription 

	FROM DimProduct; 