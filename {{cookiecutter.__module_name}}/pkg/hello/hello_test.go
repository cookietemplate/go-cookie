package hello_test

import (
	"{{cookiecutter.project_slug}}/pkg/hello"
	"testing"
)

func TestSayHello(t *testing.T) {
	helloText := hello.SayHello("John")
	if helloText != "Hello, John!" {
		t.Errorf("Unexpected return value: %s", helloText)
	}
}
