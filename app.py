#!/usr/bin/env python3

import aws_cdk as cdk

from artemis_project.artemis_project_stack import ArtemisProjectStack


app = cdk.App()
ArtemisProjectStack(app, "artemis-project")

app.synth()
