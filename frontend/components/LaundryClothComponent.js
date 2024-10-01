import React from 'react';
import { View, Text, Image, StyleSheet, TouchableOpacity } from 'react-native';

const LaundryClothComponent = () => {
    return (
        <View>  
        <View style={styles.card}>
      <Image
        source={{ uri: 'https://wallpapers.com/images/hd/naruto-uzumaki-4k-m6911vxsmy2jarn1.jpg' }} // Replace with your image URL
        style={styles.cardImage}
      />
      <View style={styles.cardContent}>
        <Text style={styles.cardTitle}>Beautiful Landscape</Text>
        <Text style={styles.cardDescription}>
          Explore the beautiful landscapes around the world. This is a sample description that shows how you can customize the text inside a card component.
        </Text>
        <TouchableOpacity style={styles.button} onPress={() => alert('View Now clicked!')}>
          <Text style={styles.buttonText}>VIEW NOW</Text>
        </TouchableOpacity>
      </View>
    </View>
        </View>
        
    );
}

const styles = StyleSheet.create({
    card: {
      backgroundColor: '#fff',
      borderRadius: 8,
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.2,
      shadowRadius: 8,
      elevation: 5,
      margin: 10,
    },
    cardImage: {
      width: '100%',
      height: 200,
      borderTopLeftRadius: 8,
      borderTopRightRadius: 8,
    },
    cardContent: {
      padding: 15,
    },
    cardTitle: {
      fontSize: 18,
      fontWeight: 'bold',
      marginBottom: 10,
    },
    cardDescription: {
      fontSize: 14,
      color: '#444',
      marginBottom: 20,
    },
    button: {
      backgroundColor: '#2196F3',
      paddingVertical: 10,
      paddingHorizontal: 15,
      borderRadius: 5,
      alignItems: 'center',
    },
    buttonText: {
      color: '#fff',
      fontWeight: 'bold',
      fontSize: 16,
    },
  });

export default LaundryClothComponent;
