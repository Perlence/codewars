module Codewars.Kata.Bus where

import Test.Hspec
import Test.QuickCheck

number :: [(Int, Int)] -> Int
number xs = foldl (\people (goIn, goOut) -> people+goIn-goOut) 0 xs

main = hspec $ describe "number" $ do
  it "returns 0 for a bus without stops" $
    number [] `shouldBe` 0

  it "returns the correct number for some examples" $ do
    number [(10, 0), (3, 5), (5,  8)] `shouldBe` 5
    number [(3, 0),  (9, 1), (4, 10), (12, 2), (6, 1), (7, 10)] `shouldBe` 17
    number [(3, 0),  (9, 1), (4,  8), (12, 2), (6, 1), (7,  8)] `shouldBe` 21
