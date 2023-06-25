package com.us.idl.ICSOC23;

import org.junit.Test;
import org.openapitools.codegen.ClientOptInput;
import org.openapitools.codegen.DefaultGenerator;
import org.openapitools.codegen.config.CodegenConfigurator;

/***
 * This test allows you to easily launch your code generation software under a debugger.
 * Then run this test under debug mode.  You will be able to step through your java code 
 * and then see the results in the out directory. 
 *
 * To experiment with debugging your code generator:
 * 1) Set a break point in JavaIdlGenerator.java in the postProcessOperationsWithModels() method.
 * 2) To launch this test in Eclipse: right-click | Debug As | JUnit Test
 *
 */
public class JavaSpringIDLCodegenTest {

  @Test
  public void launchCodeGeneratorAmadeus() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/Amadeus/swagger.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/AmadeusIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorDHL() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/DHL/openapi.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/DHLIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorFoursquare() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/Foursquare/openapi.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/FoursquareIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorOhsome() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/Ohsome/swagger.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/OhsomeIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorOMDb() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/OMDb/swagger.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/OMDbIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorTravel() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/Travel/swagger.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/TravelIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorTumblr() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/Tumblr/swagger.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/TumblrIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorYelp() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/Yelp/openapi.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/YelpIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }

  @Test
  public void launchCodeGeneratorYouTube() {
    // to understand how the 'openapi-generator-cli' module is using 'CodegenConfigurator', have a look at the 'Generate' class:
    // https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator-cli/src/main/java/org/openapitools/codegen/cmd/Generate.java
    final CodegenConfigurator configurator = new CodegenConfigurator()
            .setGeneratorName("spring-idl") // use this codegen library
            .setInputSpec("ICSOC23/OAS/YouTube/openapi.yaml") // sample OpenAPI file
            .setOutputDir("out/ICSOC23/Java/YouTubeIDL"); // output directory

    final ClientOptInput clientOptInput = configurator.toClientOptInput();
    DefaultGenerator generator = new DefaultGenerator();
    generator.opts(clientOptInput).generate();
  }
}