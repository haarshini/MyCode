import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class Movies extends JFrame
{
    public static void main(String args[])
        {
    JTextField t1,t2;
    JLabel l1,l2,l3;
    JButton b1,b2;
    {
        JFrame frame = new JFrame("Netflix.in");
        l1= new JLabel("Movie name:");
        l1.setBounds(70,80,90,60);
        l2= new JLabel("Series:");
        l2.setBounds(70,120,90,60);
        t1 =  new JTextField();
        t1.setBounds(160,100,90,20);
        t2 = new JTextField();
        t2.setBounds(160,140,90,20);
        b1 = new JButton("Watch");
        b1.setBounds(100,250,90,30);
        b2 = new JButton("Watchlist");
        b2.setBounds(180,250,90,30);
        JLabel l = new JLabel("hi enter the movie name");
        l.setBounds(100,200,200,50);
        frame.add(l1);
        frame.add(l2);
        frame.add(t1);
        frame.add(t2);
        frame.add(b1);
        frame.add(b2);
        frame.add(l);
        frame.setSize(400,400);
        frame.setLayout(null);
        frame.setVisible(true);
        b1.addActionListener(new ActionListener()
            {
            @Override
            public void actionPerformed(ActionEvent actionEvent)
            {
                l.setText(" Now watching : " +t1.getText());
            }
        });
        b2.addActionListener(new ActionListener()
            {
            @Override
            public void actionPerformed(ActionEvent actionEvent)
            {
                l.setText(t1.getText() + "  Added to Watchlist");
            }
        });
    }       
    }
}
        
   
        
