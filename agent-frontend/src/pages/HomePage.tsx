import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { generateCharacter, generateDialogue, saveDialogue, getDefaultTexts } from '../services/api';  // 导入获取默认文本的 API

// 保留 Character 接口，确保类型安全
export interface Character {
  name: string;
  age: number;
  occupation: string;
  personality_traits?: string[];  // 将 personality_traits 标记为可选
  background: string;
  goals_and_motivations?: string[];  // 将 goals_and_motivations 标记为可选
  speaking_style: string;
}

const HomePageContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: ${props => props.theme.colors.background};
  color: ${props => props.theme.colors.text};
  padding: 20px;
`;

const Title = styled.h1`
  color: ${props => props.theme.colors.primary};
  font-size: 3rem;
  margin-bottom: 2rem;
`;

const Button = styled.button`
  background-color: ${props => props.theme.colors.secondary};
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  color: ${props => props.theme.colors.text};
  transition: all 0.3s ease;

  &:hover {
    background-color: ${props => props.theme.colors.primary};
  }
`;

const TextArea = styled.textarea`
  width: 80%;
  height: 100px;
  margin: 20px 0;
  background-color: #1a1a1a;
  color: #f5f5f5;
  border: 1px solid #333;
  padding: 10px;
  border-radius: 5px;
`;

const CharacterCard = styled.div`
  background-color: #1a1a1a;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  width: 80%;
  color: #00ff99;
  border: 1px solid #00ff99;
`;

const CharacterInfo = styled.div`
  margin-bottom: 10px;
`;

const Label = styled.span`
  font-weight: bold;
  color: #00ffff;
`;

const HomePage = () => {
  const [character1, setCharacter1] = useState<Character | null>(null);
  const [character2, setCharacter2] = useState<Character | null>(null);
  const [dialogue, setDialogue] = useState(null);
  const [text1, setText1] = useState('');  // 初始化为空，稍后获取默认值
  const [text2, setText2] = useState('');  // 初始化为空，稍后获取默认值

  // 使用 useEffect 在页面加载时获取默认文本
  useEffect(() => {
    const fetchDefaultTexts = async () => {
      try {
        const response = await getDefaultTexts();  // 从后端获取默认文本
        setText1(response.text1);  // 设置文本1
        setText2(response.text2);  // 设置文本2
      } catch (error) {
        console.error('Error fetching default texts:', error);
      }
    };
    fetchDefaultTexts();
  }, []);  // 仅在组件挂载时执行一次

  const handleGenerateCharacters = async () => {
    try {
      const generatedCharacter1 = await generateCharacter(text1);  // 使用 text1 生成角色1
      const generatedCharacter2 = await generateCharacter(text2);  // 使用 text2 生成角色2
      console.log("Character 1:", generatedCharacter1);  // 添加调试信息
      console.log("Character 2:", generatedCharacter2);  // 添加调试信息
      setCharacter1(generatedCharacter1);
      setCharacter2(generatedCharacter2);
    } catch (error) {
      console.error('Failed to generate characters:', error);
    }
  };

  return (
    <HomePageContainer>
      <Title>GLM Role Agent</Title>

      <TextArea 
        value={text1} 
        onChange={e => setText1(e.target.value)} 
        placeholder={text1}  // 将获取到的默认文本作为 placeholder
      />
      <TextArea 
        value={text2} 
        onChange={e => setText2(e.target.value)} 
        placeholder={text2}  // 将获取到的默认文本作为 placeholder
      />

      <Button onClick={handleGenerateCharacters}>Generate Characters</Button>

      {character1 && character2 && (
        <>
          <div>
            <h2>Generated Characters:</h2>
            <CharacterCard>
              <CharacterInfo>
                <Label>Name:</Label> {character1.name}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Age:</Label> {character1.age}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Occupation:</Label> {character1.occupation}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Personality Traits:</Label> {character1.personality_traits?.join(', ')}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Background:</Label> {character1.background}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Goals and Motivations:</Label> {character1.goals_and_motivations?.join(', ')}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Speaking Style:</Label> {character1.speaking_style}
              </CharacterInfo>
            </CharacterCard>

            <CharacterCard>
              <CharacterInfo>
                <Label>Name:</Label> {character2.name}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Age:</Label> {character2.age}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Occupation:</Label> {character2.occupation}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Personality Traits:</Label> {character2.personality_traits?.join(', ')}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Background:</Label> {character2.background}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Goals and Motivations:</Label> {character2.goals_and_motivations?.join(', ')}
              </CharacterInfo>
              <CharacterInfo>
                <Label>Speaking Style:</Label> {character2.speaking_style}
              </CharacterInfo>
            </CharacterCard>
          </div>
        </>
      )}
    </HomePageContainer>
  );
};

export default HomePage;