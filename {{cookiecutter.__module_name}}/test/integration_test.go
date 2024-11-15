package integration_test

import (
	"{{cookiecutter.project_slug}}/internal/utils"
	"{{cookiecutter.project_slug}}/pkg/hello"
	"strings"
	"testing"
)

func TestIntegration(t *testing.T) {
	sayHello := hello.SayHello("John")
	if sayHello != "Hello, John!" {
		t.Errorf("Unexpected return value: %s", sayHello)
	}

	formatedInfos := utils.FormatInfos("MyApp", "1.0.0", "Hello, John!")
	if !strings.HasSuffix(formatedInfos, " - MyApp[1.0.0]: Hello, John!") {
		t.Errorf("Unexpected formatted string: %s", formatedInfos)
	}
}
