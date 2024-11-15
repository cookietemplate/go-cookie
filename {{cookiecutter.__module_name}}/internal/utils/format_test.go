package utils_test

import (
	"{{cookiecutter.project_slug}}/internal/utils"
	"strings"
	"testing"
)

func TestFormatInfos(t *testing.T) {
	formatedInfos := utils.FormatInfos("MyApp", "1.0.0", "Hello, John!")
	if !strings.HasSuffix(formatedInfos, " - MyApp[1.0.0]: Hello, John!") {
		t.Errorf("Unexpected formatted string: %s", formatedInfos)
	}
}
