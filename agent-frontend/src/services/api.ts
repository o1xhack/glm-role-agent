import axios from 'axios';
import { Character } from '../pages/HomePage';  // 导入 Character 接口

const API_BASE_URL = 'http://localhost:5002';

// 生成角色
export const generateCharacter = async (text: string, language: string = 'en') => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/generate_character`, { text, language });
    return response.data;
  } catch (error) {
    console.error('Error generating character:', error);
    throw error;
  }
};

// 生成对话
export const generateDialogue = async (character1: Character, character2: Character, topic: string, language: string = 'en') => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/generate_dialogue`, { character1, character2, topic, language });
    return response.data;
  } catch (error) {
    console.error('Error generating dialogue:', error);
    throw error;
  }
};

// 保存对话
export const saveDialogue = async (characters: Character[], dialogues: any[]) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/save_dialogue`, { characters, dialogues });
    return response.data;
  } catch (error) {
    console.error('Error saving dialogue:', error);
    throw error;
  }
};

// 获取默认文本
export const getDefaultTexts = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/get_default_texts`);
    return response.data;
  } catch (error) {
    console.error('Error fetching default texts:', error);
    throw error;
  }
};