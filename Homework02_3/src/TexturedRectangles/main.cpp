#include <fstream>
#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "../utils/shader_utils.h"
#include "../utils/texture.h"

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

int main(void)
{
    GLFWwindow* window;

    if (!glfwInit()) return -1;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    window = glfwCreateWindow(800, 600, "Task 1: Three Textured Rectangles", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) return -1;

    // Світло-сірий фон
    glClearColor(0.9f, 0.9f, 0.9f, 1.0f);

    std::string vShader = "res/shaders/rect.vert";
    std::string fShader = "res/shaders/rect.frag";
    GLuint shaderProgram = createProgram(vShader, fShader);

    GLint texture_loc = glGetUniformLocation(shaderProgram, "uTexture");
    GLint transform_loc = glGetUniformLocation(shaderProgram, "uTransformation");

    float vertices[] = {
        -0.2f, -0.4f,  0.0f, 0.0f,
         0.2f, -0.4f,  1.0f, 0.0f,
         0.2f,  0.4f,  1.0f, 1.0f,
        -0.2f,  0.4f,  0.0f, 1.0f
    };
    unsigned int indices[] = { 0, 1, 2, 0, 2, 3 };

    GLuint VBO, indexBuffer, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &indexBuffer);

    glBindVertexArray(VAO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    // Координати
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // UV (текстури)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));
    glEnableVertexAttribArray(1);

    unsigned int tex1 = loadTexture("res/textures/picture.jpg");
    unsigned int tex2 = loadTexture("res/textures/picture2.jpg");
    unsigned int tex3 = loadTexture("res/textures/picture4.jpg");

    while (!glfwWindowShouldClose(window) && !glfwGetKey(window, GLFW_KEY_ESCAPE))
    {
        glClear(GL_COLOR_BUFFER_BIT);
        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);

        glm::mat4 model1 = glm::translate(glm::mat4(1.0f), glm::vec3(-0.6f, 0.0f, 0.0f));
        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, glm::value_ptr(model1));
        glBindTexture(GL_TEXTURE_2D, tex1);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        glm::mat4 model2 = glm::translate(glm::mat4(1.0f), glm::vec3(0.0f, 0.0f, 0.0f));
        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, glm::value_ptr(model2));
        glBindTexture(GL_TEXTURE_2D, tex2);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        glm::mat4 model3 = glm::translate(glm::mat4(1.0f), glm::vec3(0.6f, 0.0f, 0.0f));
        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, glm::value_ptr(model3));
        glBindTexture(GL_TEXTURE_2D, tex3);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteBuffers(1, &VBO);
    glDeleteBuffers(1, &indexBuffer);
    glDeleteVertexArrays(1, &VAO);
    glfwTerminate();
    return 0;
}