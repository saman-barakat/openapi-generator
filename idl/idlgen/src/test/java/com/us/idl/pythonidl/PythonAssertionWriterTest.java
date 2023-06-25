package com.us.idl.pythonidl;

import com.us.idl.CodegenDependency;
import com.us.idl.pythonidl.PythonFastApiIDLCodegen;
import io.swagger.parser.OpenAPIParser;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.parser.core.models.ParseOptions;
import org.junit.Assert;
import org.junit.Test;
import org.openapitools.codegen.CodegenOperation;

import java.util.List;

public class PythonAssertionWriterTest {

    @Test
    public void generateAssertions(){
        OpenAPI openAPI = new OpenAPIParser().readLocation("example.yaml", null, new ParseOptions()).getOpenAPI();
        PythonFastApiIDLCodegen codegen = new PythonFastApiIDLCodegen();

        String path = "/example1/simple";
        Operation operation = openAPI.getPaths().get(path).readOperations().get(0);
        CodegenOperation op = codegen.fromOperation(path,"get",operation,openAPI.getServers());

        List<CodegenDependency> dependencies = (List<CodegenDependency>) op.vendorExtensions.get("x-dependencies");

        for (CodegenDependency dep: dependencies){
            Assert.assertNotNull(dep.assertOperation);
            System.out.println("Dependency: " + dep.idlDependency + "\n\t Assertion: " + dep.assertOperation);
        }
    }

    @Test
    public void generateComplexAssertions(){
        OpenAPI openAPI = new OpenAPIParser().readLocation("example.yaml", null, new ParseOptions()).getOpenAPI();
        PythonFastApiIDLCodegen codegen = new PythonFastApiIDLCodegen();

        String path = "/example1/complex";
        Operation operation = openAPI.getPaths().get(path).readOperations().get(0);
        CodegenOperation op = codegen.fromOperation(path,"get",operation,openAPI.getServers());

        List<CodegenDependency> dependencies = (List<CodegenDependency>) op.vendorExtensions.get("x-dependencies");

        for (CodegenDependency dep: dependencies){
            Assert.assertNotNull(dep.assertOperation);
            System.out.println("Dependency: " + dep.idlDependency + "\n\t Assertion: " + dep.assertOperation);
        }
    }
}
