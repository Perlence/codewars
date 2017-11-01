module Codewars.Kata.Sheep where

import Test.Hspec
import Test.QuickCheck ((==>))

countSheep :: [Bool] -> Int
countSheep = length . (filter ((==) True))

main = hspec $ do
  describe "countSheep" $ do
    it "should work for some examples" $ do
      countSheep []            `shouldBe` 0
      countSheep [True]        `shouldBe` 1
      countSheep [True,False]  `shouldBe` 1
      countSheep [False,False] `shouldBe` 0
