terraform {
    backend "remote" {
        organization = "stefanoborini"
        workspaces {
            name = "test"
        }
    }
}

resource "random_pet" "random_value" {
    length = 2
}

provider "heroku" {
    email = ""
    api_key = ""
}

resource "heroku_app" "default-2" {
  name   = "cool-app-${random_pet.random_value.id}"
  region = "${var.region}"

  config_vars {
    FOOBAR = "${var.foo}"
  }

  buildpacks = [
    "heroku/go"
  ]
}

resource "heroku_app" "default-3" {
  name = "cool-app-2-${random_pet.random_value.id}"
  region = "${var.region}"
  depends_on = ["heroku_app.default-2"] 
  count = 1
  provisioner "local-exec" {
    command = "echo hello >> private_ips.txt"
  }
  config_vars {
    FOOBAR = "${var.foo}"
  }

  buildpacks = [
    "heroku/go"
  ]
}

output "random_value" {
    value = "${random_pet.random_value.id}"
}

output "whatever" {
    value = "${var.region}"
}

output "whatever2" {
    value = "${var.foo}"
}
