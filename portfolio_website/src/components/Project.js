import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

/**
 * Project component displays individual project details including title, description, and tech stack.
 * @param {Object} props
 * @param {string} props.id - Unique identifier of the project
 * @param {string} props.title - Project title
 * @param {string} props.description - Brief description of the project
 * @param {string[]} props.techStack - List of technologies used
 * @returns {JSX.Element} Rendered project component
 * 
 * @example
 * <Project
 *   id="1"
 *   title="Project One"
 *   description="This is a sample project."
 *   techStack={["React", "Node.js"]}
 * />
 */
const ProjectWrapper = styled.div`
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  background-color: #fafafa;
`;

const Title = styled.h2`
  margin: 0 0 0.5rem 0;
`;

const Description = styled.p`
  margin: 0 0 0.5rem 0;
`;

const TechList = styled.ul`
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
`;

const TechItem = styled.li`
  background-color: #007acc;
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.875rem;
`;

function Project({ id, title, description, techStack }) {
  if (!id || !title || !description || !Array.isArray(techStack)) {
    console.error('Invalid properties supplied to Project component');
    return null;
  }

  return (
    <ProjectWrapper aria-labelledby={`project-${id}-title`} role="region">
      <Title id={`project-${id}-title`}>{title}</Title>
      <Description>{description}</Description>
      <TechList>
        {techStack.map((tech) => (
          <TechItem key={tech}>{tech}</TechItem>
        ))}
      </TechList>
    </ProjectWrapper>
  );
}

Project.propTypes = {
  id: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  techStack: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Project;
