import XCTest

import testCodeTests

var tests = [XCTestCaseEntry]()
tests += testCodeTests.allTests()
XCTMain(tests)
